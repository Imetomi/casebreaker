import { RetryError } from './errors';

const API_BASE_URL = (process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000') + '/api/v1';
const MAX_RETRIES = 3;
const RETRY_DELAY = 1000; // 1 second

export interface CaseStudy {
  id: number;
  title: string;
  description: string;
  checkpoints: Array<{
    id: string;
    title: string;
    content: string;
  }>;
}

interface ApiErrorResponse {
  detail: string;
}

export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
  checkpoint_id?: string;
}

export interface Session {
  id: number;
  case_study_id: number;
  device_id: string;
  created_at: string;
}

export class ApiClient {
  private async fetchWithRetry(
    url: string,
    options: RequestInit,
    retries = MAX_RETRIES
  ): Promise<Response> {
    try {
      const response = await fetch(url, options);
      
      if (!response.ok) {
        const error = await response.json() as ApiErrorResponse;
        throw new Error(error.detail || `HTTP error! status: ${response.status}`);
      }
      
      return response;
    } catch (error) {
      if (retries > 0 && error instanceof Error && !error.message.includes('404')) {
        await new Promise(resolve => setTimeout(resolve, RETRY_DELAY));
        return this.fetchWithRetry(url, options, retries - 1);
      }
      throw error instanceof Error ? error : new Error('Unknown error occurred');
    }
  }

  async createSession(caseStudyId: number, deviceId: string): Promise<Session> {
    const response = await this.fetchWithRetry(
      `${API_BASE_URL}/sessions`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          case_study_id: caseStudyId,
          device_id: deviceId,
        }),
      }
    );

    return response.json();
  }

  async sendMessage(
    sessionId: number,
    content: string,
    checkpointId: string
  ): Promise<ReadableStream<Uint8Array> | null> {
    const response = await this.fetchWithRetry(
      `${API_BASE_URL}/sessions/${sessionId}/messages`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          role: 'user',
          content,
          checkpoint_id: checkpointId,
        }),
      }
    );

    return response.body;
  }

  async getMessages(sessionId: number): Promise<ChatMessage[]> {
    const response = await this.fetchWithRetry(
      `${API_BASE_URL}/sessions/${sessionId}/messages`,
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );

    return response.json();
  }

  async completeCheckpoint(
    sessionId: number,
    checkpointId: string
  ): Promise<void> {
    await this.fetchWithRetry(
      `${API_BASE_URL}/sessions/${sessionId}/checkpoints/${checkpointId}/complete`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
  }

  async getCaseStudy(caseId: number): Promise<CaseStudy> {
    const response = await this.fetchWithRetry(
      `${API_BASE_URL}/case-studies/${caseId}`,
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );

    return response.json();
  }
}

export const api = new ApiClient();
