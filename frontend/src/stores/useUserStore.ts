import { defineStore } from 'pinia'

interface User {
  id: number
  name: string
  matric_no: string
  department: string
  level: string
}

interface State {
  user: User | null
}

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
