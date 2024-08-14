import { defineStore } from 'pinia'
import type { State, User } from '@/types'

export const useUserStore = defineStore('user', {
  state: (): State => ({
    user: null
  }),
  actions: {
    currentUser(user: User) {
      this.user = user
    },
    login(user: User) {
      this.user = user
    },
    logout() {
      this.user = null
    }
  },
  getters: {
    isAuthenticated: (state) => !!state.user
  }
})
