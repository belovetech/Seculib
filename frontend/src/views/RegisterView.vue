<template>
  <div
    class="flex justify-center items-center h-screen bg-gradient-to-r from-blue-500 to-green-500"
  >
    <div class="w-full max-w-lg bg-white shadow-lg rounded-lg p-8">
      <h2 class="text-3xl font-extrabold mb-6 text-center text-gray-800">Student Registration</h2>
      <form @submit.prevent="register">
        <div class="mb-4">
          <label for="name" class="block text-gray-700 text-sm font-bold mb-2">Full Name:</label>
          <input
            v-model="name"
            id="name"
            type="text"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div class="mb-4">
          <label for="matricNo" class="block text-gray-700 text-sm font-bold mb-2"
            >Matric Number:</label
          >
          <input
            v-model="matricNo"
            id="matricNo"
            type="text"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div class="mb-4">
          <label for="department" class="block text-gray-700 text-sm font-bold mb-2"
            >Department:</label
          >
          <input
            v-model="department"
            id="department"
            type="text"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div class="mb-4">
          <label for="level" class="block text-gray-700 text-sm font-bold mb-2">Level:</label>
          <select
            v-model="level"
            id="level"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          >
            <option value="ND 1">ND 1</option>
            <option value="ND 2">ND 2</option>
            <option value="HND 1">HND 1</option>
            <option value="HND 2">HND 2</option>
          </select>
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
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
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
import axios, { AxiosError } from 'axios'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'RegisterView',
  setup() {
    const router = useRouter()
    const name = ref('')
    const matricNo = ref('')
    const department = ref('')
    const level = ref('')
    const email = ref('')
    const password = ref('')
    const confirmPassword = ref('')
    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1/students'

    const register = async () => {
      if (password.value !== confirmPassword.value) {
        alert('Passwords do not match!')
        return
      }

      try {
        const response = await axios.post(`${BASE_URL}/register`, {
          name: name.value,
          matric_no: matricNo.value,
          department: department.value,
          level: level.value,
          email: email.value,
          password: password.value
        })
        console.log(response.data)
        const message = response.data.message
        alert(message)
        router.push('/login')
      } catch (e) {
        const error = e as AxiosError
        const data = error.response?.data as { message: string }
        alert('An error occurred. Please try again.')
        console.error(data.message)
      }
    }

    return {
      name,
      matricNo,
      department,
      level,
      email,
      password,
      confirmPassword,
      register
    }
  }
})
</script>

<style scoped>
/* Custom styles (if needed) */
</style>
