<template>
  <div class="flex justify-center items-center h-screen">
    <div class="w-full max-w-md bg-gray-800 shadow-lg rounded-lg p-8">
      <h2 class="text-3xl font-extrabold mb-6 text-center text-white">Login</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label for="matricNo" class="block text-white text-sm font-bold mb-2">Matric No:</label>
          <input
            v-model="matricNo"
            id="matricNo"
            type="text"
            class="shadow appearance-none border border-gray-600 rounded w-full py-2 px-3 text-gray-300 leading-tight focus:outline-none focus:shadow-outline bg-gray-700"
            required
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block text-white text-sm font-bold mb-2">Password:</label>
          <input
            v-model="password"
            id="password"
            type="password"
            class="shadow appearance-none border border-gray-600 rounded w-full py-2 px-3 text-gray-300 leading-tight focus:outline-none focus:shadow-outline bg-gray-700"
            required
          />
        </div>
        <div class="flex items-center justify-between">
          <button
            :disabled="loading"
            type="submit"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
          >
            <span> {{ loading ? 'Loading...' : 'Login' }}</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios, { AxiosError } from 'axios'

export default defineComponent({
  name: 'LoginView',
  setup() {
    const router = useRouter()
    const matricNo = ref('')
    const password = ref('')
    const loading = ref(false) // Loading state
    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1/students'

    const login = async () => {
      if (loading.value) return // Prevent multiple requests

      loading.value = true // Set loading to true

      try {
        const response = await axios.post(`${BASE_URL}/login`, {
          matric_no: matricNo.value,
          password: password.value
        })

        const { token } = response.data.data
        localStorage.setItem('token', token)
        router.push('/profile')
      } catch (e) {
        const error = e as AxiosError
        const message = (error.response?.data as { message: string })?.message || 'Login failed'
        alert(message)
      } finally {
        loading.value = false // Set loading to false after request is done
      }
    }

    return {
      matricNo,
      password,
      loading,
      login
    }
  }
})
</script>

<style scoped>
/* Custom styles (if needed) */
</style>
