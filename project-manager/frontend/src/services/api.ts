import axios from 'axios'

const api = axios.create({
  baseURL: '',
  headers: {
    'Content-Type': 'application/json',
  },
})

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired or invalid
      localStorage.removeItem('auth-storage')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default api

// API helper functions
export const projectApi = {
  getAll: (params?: Record<string, unknown>) => api.get('/api/v1/projects', { params }),
  getById: (id: number) => api.get(`/api/v1/projects/${id}`),
  create: (data: Record<string, unknown>) => api.post('/api/v1/projects', data),
  update: (id: number, data: Record<string, unknown>) => api.put(`/api/v1/projects/${id}`, data),
  delete: (id: number) => api.delete(`/api/v1/projects/${id}`),
  getGantt: (id: number) => api.get(`/api/v1/projects/${id}/gantt`),
  getCriticalPath: (id: number) => api.get(`/api/v1/projects/${id}/critical-path`),
}

export const boardApi = {
  getAll: (params?: Record<string, unknown>) => api.get('/api/v1/boards', { params }),
  getById: (id: number, params?: Record<string, unknown>) => api.get(`/api/v1/boards/${id}`, { params }),
  create: (data: Record<string, unknown>) => api.post('/api/v1/boards', data),
  update: (id: number, data: Record<string, unknown>) => api.put(`/api/v1/boards/${id}`, data),
}

export const taskApi = {
  getAll: (params?: Record<string, unknown>) => api.get('/api/v1/tasks', { params }),
  getById: (id: number) => api.get(`/api/v1/tasks/${id}`),
  create: (data: Record<string, unknown>) => api.post('/api/v1/tasks', data),
  update: (id: number, data: Record<string, unknown>) => api.put(`/api/v1/tasks/${id}`, data),
  delete: (id: number) => api.delete(`/api/v1/tasks/${id}`),
  reorder: (data: Record<string, unknown>) => api.post('/api/v1/tasks/reorder', data),
  addComment: (taskId: number, content: string) => api.post(`/api/v1/tasks/${taskId}/comments`, { content }),
  addTimeEntry: (taskId: number, data: Record<string, unknown>) => api.post(`/api/v1/tasks/${taskId}/time-entries`, data),
}

export const resourceApi = {
  getWorkload: (params?: Record<string, unknown>) => api.get('/api/v1/resources/workload', { params }),
  getForecast: (params?: Record<string, unknown>) => api.get('/api/v1/resources/forecast', { params }),
  allocate: (data: Record<string, unknown>) => api.post('/api/v1/resources/allocate', data),
}

export const riskApi = {
  getAll: (params?: Record<string, unknown>) => api.get('/api/v1/risks', { params }),
  getById: (id: number) => api.get(`/api/v1/risks/${id}`),
  create: (data: Record<string, unknown>) => api.post('/api/v1/risks', data),
  update: (id: number, data: Record<string, unknown>) => api.put(`/api/v1/risks/${id}`, data),
  getMatrix: (params?: Record<string, unknown>) => api.get('/api/v1/risks/matrix', { params }),
}

export const reportApi = {
  getPortfolio: (id: number) => api.get(`/api/v1/reports/portfolio/${id}`),
  getProject: (id: number) => api.get(`/api/v1/reports/project/${id}`),
  getResourceUtilization: (params?: Record<string, unknown>) => api.get('/api/v1/reports/resource-utilization', { params }),
  getRiskSummary: (params?: Record<string, unknown>) => api.get('/api/v1/reports/risk-summary', { params }),
  getVelocity: (params?: Record<string, unknown>) => api.get('/api/v1/reports/velocity', { params }),
  getBurndown: (projectId: number) => api.get(`/api/v1/reports/burndown/${projectId}`),
}

export const userApi = {
  getAll: (params?: Record<string, unknown>) => api.get('/api/v1/users', { params }),
  getById: (id: number) => api.get(`/api/v1/users/${id}`),
  getWorkload: (id: number, params?: Record<string, unknown>) => api.get(`/api/v1/users/${id}/workload`, { params }),
}

export const templateApi = {
  getAll: (params?: Record<string, unknown>) => api.get('/api/v1/templates', { params }),
  apply: (templateId: number, projectId: number) => api.post(`/api/v1/templates/${templateId}/apply`, { project_id: projectId }),
}
