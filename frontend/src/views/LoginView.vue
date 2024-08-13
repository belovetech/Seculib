<template>
  <div class="flex justify-center items-center h-screen bg-gray-100">
    <div class="w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-center">Login</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label for="email" class="block text-gray-700 text-sm font-bold mb-2">Email:</label>
          <input
            v-model="email"
            id="email"
            type="email"
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
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
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
import axios from 'axios'

export default defineComponent({
  name: 'LoginView',
  setup() {
    const email = ref('')
    const password = ref('')

    const userStore = useUserStore()

    const login = async () => {
      try {
        const response = await axios.post('your-backend-api/login', {
          email: email.value,
          password: password.value
        })
        userStore.login(response.data)
        // Handle successful login, like redirecting to books list
      } catch (error) {
        // Handle error
      }
    }

    return {
      email,
      password,
      login
    }
  }
})
</script>
