import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import api from '../services/api'

interface User {
  id: number
  email: string
  name: string
  role: string
  avatar_url?: string
}

interface AuthState {
  user: User | null
  token: string | null
  isAuthenticated: boolean
  login: (email: string, password: string) => Promise<void>
  register: (email: string, password: string, name: string) => Promise<void>
  logout: () => void
  updateUser: (data: Partial<User>) => void
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      user: null,
      token: null,
      isAuthenticated: false,

      login: async (email: string, password: string) => {
        const response = await api.post('/api/v1/auth/login', { email, password })
        const { user, access_token } = response.data

        set({
          user,
          token: access_token,
          isAuthenticated: true,
        })

        // Set token in API defaults
        api.defaults.headers.common['Authorization'] = `Bearer ${access_token}`
      },

      register: async (email: string, password: string, name: string) => {
        const response = await api.post('/api/v1/auth/register', {
          email,
          password,
          name,
        })
        const { user, access_token } = response.data

        set({
          user,
          token: access_token,
          isAuthenticated: true,
        })

        api.defaults.headers.common['Authorization'] = `Bearer ${access_token}`
      },

      logout: () => {
        set({
          user: null,
          token: null,
          isAuthenticated: false,
        })
        delete api.defaults.headers.common['Authorization']
      },

      updateUser: (data: Partial<User>) => {
        const currentUser = get().user
        if (currentUser) {
          set({ user: { ...currentUser, ...data } })
        }
      },
    }),
    {
      name: 'auth-storage',
      partialize: (state) => ({
        user: state.user,
        token: state.token,
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
)

// Initialize token on app load
const token = useAuthStore.getState().token
if (token) {
  api.defaults.headers.common['Authorization'] = `Bearer ${token}`
}
