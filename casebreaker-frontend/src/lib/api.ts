import { RetryError } from './errors';

const API_BASE_URL = (process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000') + '/api/v1';
const MAX_RETRIES = 3;
const RETRY_DELAY = 1000; // 1 second

// API response types
interface ApiCaseStudy {
  id: number;
  title: string;
  description: string;
  difficulty: number;
  estimated_time: number;
}

// Mapped types for frontend
export interface CaseStudyListItem {
  id: number;
  title: string;
  description: string;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  estimatedTime: string;
}

// Utility functions for data transformation
const mapDifficulty = (level: number): 'Beginner' | 'Intermediate' | 'Advanced' => {
  const mapping = {
    1: 'Beginner',
    2: 'Intermediate',
    3: 'Advanced'
  } as const;
  return mapping[level as keyof typeof mapping] || 'Intermediate';
};

const formatEstimatedTime = (minutes: number): string => {
  return `${minutes} min`;
};

interface ApiCheckpoint {
  id: string;
  title: string;
  description: string;
  hints: string[];
}

interface ApiContextMaterials {
  background: string;
  key_concepts: string[];
  required_reading: string;
}

interface ApiCaseStudyDetail extends ApiCaseStudy {
  specialization: string;
  learning_objectives: string[];
  context_materials: ApiContextMaterials;
  checkpoints: ApiCheckpoint[];
  source_url: string;
  source_type: string;
  share_slug: string;
  last_updated: string;
  created_at: string;
  subtopic: Subtopic;
}

export interface CaseStudy extends CaseStudyListItem {
  specialization: string;
  learningObjectives: string[];
  contextMaterials: {
    background: string;
    keyConcepts: string[];
    requiredReading: string;
  };
  checkpoints: Array<{
    id: string;
    title: string;
    description: string;
    hints: string[];
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

export interface Field {
  id: number;
  name: string;
  description: string;
  icon_url: string | null;
}

export interface Subtopic {
  id: number;
  name: string;
  description: string;
  field_id: number;
  field: Field;
  case_count: number;
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
          'accept': 'application/json',
        },
      }
    );

    if (!response.ok) {
      throw new Error('Failed to fetch case study');
    }

    const apiCase = await response.json() as ApiCaseStudyDetail;
    
    return {
      id: apiCase.id,
      title: apiCase.title,
      description: apiCase.description,
      difficulty: mapDifficulty(apiCase.difficulty),
      estimatedTime: formatEstimatedTime(apiCase.estimated_time),
      specialization: apiCase.specialization || '',
      learningObjectives: apiCase.learning_objectives || [],
      contextMaterials: {
        background: apiCase.context_materials?.background || '',
        keyConcepts: apiCase.context_materials?.key_concepts || [],
        requiredReading: apiCase.context_materials?.required_reading || '',
      },
      checkpoints: apiCase.checkpoints || [],
    };
  }

  async getField(fieldId: number): Promise<Field> {
    const response = await this.fetchWithRetry(`${API_BASE_URL}/fields/${fieldId}`, {
      method: 'GET',
    });
    
    if (!response.ok) {
      throw new Error('Failed to fetch field');
    }
    
    return response.json();
  }

  async getSubtopics(fieldId: number): Promise<Subtopic[]> {
    const response = await this.fetchWithRetry(`${API_BASE_URL}/subtopics/?field_id=${fieldId}`, {
      method: 'GET',
    });
    
    if (!response.ok) {
      throw new Error('Failed to fetch subtopics');
    }
    
    return response.json();
  }

  async getCaseStudiesBySubtopic(subtopicId: number): Promise<CaseStudyListItem[]> {
    const response = await this.fetchWithRetry(`${API_BASE_URL}/case-studies/?subtopic_id=${subtopicId}`, {
      method: 'GET',
      headers: {
        'accept': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error('Failed to fetch case studies');
    }

    const apiCases = await response.json() as ApiCaseStudy[];
    
    return apiCases.map(apiCase => ({
      id: apiCase.id,
      title: apiCase.title,
      description: apiCase.description,
      difficulty: mapDifficulty(apiCase.difficulty),
      estimatedTime: formatEstimatedTime(apiCase.estimated_time)
    }));
  }
}

export const api = new ApiClient();
