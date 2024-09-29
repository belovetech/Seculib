<!-- bg-black -->
<template>
  <div class="flex justify-center items-center min-h-screen p-4">
    <div class="w-full max-w-xl bg-gray-800 shadow-lg rounded-lg p-8">
      <h2 class="text-3xl font-extrabold mb-6 text-center text-white">Registration</h2>
      <form @submit.prevent="register">
        <div class="mb-4">
          <label for="name" class="block text-white text-sm font-bold mb-2">Full Name:</label>
          <input
            v-model="name"
            id="name"
            type="text"
            class="shadow appearance-none border border-gray-600 rounded w-full py-2 px-3 text-gray-300 leading-tight focus:outline-none focus:shadow-outline bg-gray-700"
            required
          />
        </div>
        <div class="mb-4">
          <label for="matricNo" class="block text-white text-sm font-bold mb-2"
            >Matric Number:</label
          >
          <input
            v-model="matricNo"
            id="matricNo"
            type="text"
            class="shadow appearance-none border border-gray-600 rounded w-full py-2 px-3 text-gray-300 leading-tight focus:outline-none focus:shadow-outline bg-gray-700"
            required
          />
        </div>
        <div class="mb-4">
          <label for="department" class="block text-white text-sm font-bold mb-2"
            >Department:</label
          >
          <input
            v-model="department"
            id="department"
            type="text"
            class="shadow appearance-none border border-gray-600 rounded w-full py-2 px-3 text-gray-300 leading-tight focus:outline-none focus:shadow-outline bg-gray-700"
            required
          />
        </div>
        <div class="mb-4">
          <label for="level" class="block text-white text-sm font-bold mb-2">Level:</label>
          <select
            v-model="level"
            id="level"
            class="shadow appearance-none border border-gray-600 rounded w-full py-2 px-3 text-gray-300 leading-tight focus:outline-none focus:shadow-outline bg-gray-700"
            required
          >
            <option value="ND 1">ND 1</option>
            <option value="ND 2">ND 2</option>
            <option value="HND 1">HND 1</option>
            <option value="HND 2">HND 2</option>
          </select>
        </div>
        <div class="mb-4">
          <label for="password" class="block text-white text-sm font-bold mb-2">Password:</label>
          <input
            v-model="password"
            id="password"
            type="password"
            class="shadow appearance-none border border-gray-600 rounded w-full py-2 px-3 text-gray-300 leading-tight focus:outline-none focus:shadow-outline bg-gray-700"
            required
          />
        </div>
        <div class="mb-6">
          <label for="confirmPassword" class="block text-white text-sm font-bold mb-2"
            >Confirm Password:</label
          >
          <input
            v-model="confirmPassword"
            id="confirmPassword"
            type="password"
            class="shadow appearance-none border border-gray-600 rounded w-full py-2 px-3 text-gray-300 leading-tight focus:outline-none focus:shadow-outline bg-gray-700"
            required
          />
          <span v-if="isError" class="text-red-600 text-xs font-semibold">{{ errorMsg }}</span>
        </div>
        <div class="flex items-center justify-between">
          <button
            :disabled="loading"
            type="submit"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
          >
            <span>{{ loading ? 'Loading...' : 'Register' }}</span>
          </button>
        </div>
      </form>
      <div class="mt-4 text-center">
        <p class="text-gray-300">Already have an account?</p>
        <button
          @click="goToLogin"
          class="mt-2 bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Login
        </button>
      </div>
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
    const password = ref('')
    const confirmPassword = ref('')

    const loading = ref(false)
    const isError = ref(false)
    const errorMsg = ref('')

    const BASE_URL = 'https://secure-auth-dos-prevention.onrender.com/api/v1/students'

    const register = async () => {
      if (loading.value) return

      loading.value = true

      if (password.value !== confirmPassword.value) {
        isError.value = true
        errorMsg.value = 'Passwords do not match!'
        loading.value = false
        return
      }

      try {
        await axios.post(`${BASE_URL}/register`, {
          name: name.value,
          matric_no: matricNo.value,
          department: department.value,
          level: level.value,
          password: password.value
        })

        router.push('/login')

        // Todo: store token and redirect to /books
      } catch (e) {
        const error = e as AxiosError
        const data = error.response?.data as { message: string }
        isError.value = true
        errorMsg.value = data.message
      } finally {
        loading.value = false
      }
    }

    const goToLogin = () => {
      router.push('/login')
    }

    return {
      name,
      matricNo,
      department,
      level,
      password,
      confirmPassword,
      loading,
      errorMsg,
      isError,
      register,
      goToLogin
    }
  }
})
</script>

<style scoped>
/* Custom styles (if needed) */
</style>
