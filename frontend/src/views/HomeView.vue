<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HomeView'
})
</script>

<template>
  <div class="text-center py-20">
    <h1 class="text-4xl font-bold">Welcome to the E-Library</h1>
    <p class="mt-4">Access a wide range of books. Register, Login, and Start Borrowing!</p>
    <div class="mt-8">
      <router-link to="/register" class="bg-blue-500 text-white py-2 px-4 rounded"
        >Register</router-link
      >
      <router-link to="/login" class="bg-green-500 text-white py-2 px-4 rounded ml-4"
        >Login</router-link
      >
    </div>
  </div>
</template>
