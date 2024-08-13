import { defineStore } from 'pinia'

interface User {
  id: number
  name: string
  email: string
}

interface State {
  user: User | null
}

export const useUserStore = defineStore('user', {
  state: (): State => ({
    user: null
  }),
  actions: {
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
