<template>
  <div
    class="flex justify-center items-center h-screen bg-gradient-to-r from-green-500 to-blue-500"
  >
    <div class="w-full max-w-lg bg-white shadow-lg rounded-lg p-8">
      <h2 class="text-3xl font-extrabold mb-6 text-center text-gray-800">Login</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label for="matricNo" class="block text-gray-700 text-sm font-bold mb-2">matricNo:</label>
          <input
            v-model="matricNo"
            id="matricNo"
            type="text"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-gray-700 text-sm font-bold mb-2">Password:</label>
          <input
            v-model="password"
            id="password"
            type="password"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div class="flex items-center justify-between">
          <button
            type="submit"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
          >
            Login
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useUserStore } from '@/stores/useUserStore'
import axios, { AxiosError } from 'axios'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'LoginView',
  setup() {
    const router = useRouter()
    const matricNo = ref('')
    const password = ref('')
    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1/students'
    const userStore = useUserStore()

    const login = async () => {
      try {
        const response = await axios.post(`${BASE_URL}/login`, {
          matric_no: matricNo.value,
          password: password.value
        })
        // userStore.login(response.data)
        // localStorage.setItem('token', response.data.token)
        const message = response.data.message
        alert(message)
        router.push('/books')
      } catch (e) {
        const error = e as AxiosError
        const message = error.response?.data as { message: string }
        alert(message.message)
        console.error(error)
      }
    }

    return {
      matricNo,
      password,
      login
    }
  }
})
</script>

<style scoped>
/* Custom styles (if needed) */
</style>
