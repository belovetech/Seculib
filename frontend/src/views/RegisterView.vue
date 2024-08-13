<template>
  <div class="flex justify-center items-center h-screen bg-gray-100">
    <div class="w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-center">Register</h2>
      <form @submit.prevent="register">
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
        <div class="mb-4">
          <label for="password" class="block text-gray-700 text-sm font-bold mb-2">Password:</label>
          <input
            v-model="password"
            id="password"
            type="password"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div class="mb-6">
          <label for="confirmPassword" class="block text-gray-700 text-sm font-bold mb-2"
            >Confirm Password:</label
          >
          <input
            v-model="confirmPassword"
            id="confirmPassword"
            type="password"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div class="flex items-center justify-between">
          <button
            type="submit"
            class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Register
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import axios from 'axios'

export default defineComponent({
  name: 'RegisterView',
  setup() {
    const email = ref('')
    const password = ref('')
    const confirmPassword = ref('')

    const register = async () => {
      if (password.value !== confirmPassword.value) {
        alert('Passwords do not match!')
        return
      }

      try {
        const response = await axios.post('your-backend-api/register', {
          email: email.value,
          password: password.value
        })
        // Handle successful registration (e.g., redirect to login)
      } catch (error) {
        // Handle error
      }
    }

    return {
      email,
      password,
      confirmPassword,
      register
    }
  }
})
</script>
