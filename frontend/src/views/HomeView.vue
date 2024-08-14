<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HomeView'
})
</script>

<template>
  <div class="flex flex-col justify-center items-center min-h-screen bg-gray-900 text-center">
    <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold text-white">
      Welcome to Seculib
      <img
        src="../assets/white-logo.svg"
        alt="Logo"
        class="h-10 w-10 sm:h-12 sm:w-12 inline-block ml-2"
      />
    </h1>
    <p class="mt-4 text-gray-300 sm:text-lg">
      Access a wide range of books. Register, Login, and Start Borrowing!
    </p>
    <div class="mt-8 flex flex-col sm:flex-row gap-4">
      <router-link
        to="/register"
        class="bg-blue-500 text-white py-2 px-6 rounded hover:bg-blue-700 transition"
      >
        Register
      </router-link>
      <router-link
        to="/login"
        class="bg-green-500 text-white py-2 px-6 rounded hover:bg-green-700 transition"
      >
        Login
      </router-link>
    </div>
  </div>
</template>
