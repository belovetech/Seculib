import { defineStore } from 'pinia'
import type { State, User } from '@/types'
import axios, { AxiosError } from 'axios'
// import { useRouter } from 'vue-router'

const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1'

export const useUserStore = defineStore('user', {
  state: (): State => ({
    user: null,
    borrowedBooks: { borrowed_books: [], count: 0 },
    isUserAuthenticated: !!localStorage.getItem('token'),
    isAdmin: false
  }),
  actions: {
    currentUser(user: User) {
      this.user = user
    },
    login(user: User) {
      this.user = user
      this.isUserAuthenticated = true
    },
    logout() {
      localStorage.removeItem('token')
      this.user = null
      this.isUserAuthenticated = false
    },

    async getUserProfile() {
      try {
        const token = localStorage.getItem('token')
        if (!token) throw new Error('Token not found')

        const response = await axios.get(`${BASE_URL}/students/profile`, {
          headers: { Authorization: `Bearer ${token}` }
        })

        this.user = response.data.data
      } catch (e) {
        const error = e as AxiosError
        if (error.response?.status === 401) {
          console.error('Unauthorized')
          this.logout()
          // this.router.push('/login')
        }
        console.error('Error fetching profile:', e)
      }
    },

    async borrowedBook() {
      try {
        const token = localStorage.getItem('token')
        if (!token) throw new Error('Token not found')

        const response = await axios.get(`${BASE_URL}/books/borrowed`, {
          headers: { Authorization: `Bearer ${token}` }
        })

        this.borrowedBooks = response.data.data
      } catch (error) {
        console.error('Error fetching borrowed books:', error)
      }
    }
  },
  getters: {
    isAuthenticated: (state) => !!state.user,
    isAdmin: (state) => state.isAdmin
  }
})
