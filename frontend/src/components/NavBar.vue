<template>
  <nav v-if="showNavbar" class="bg-blue-600 text-white py-4 px-6 flex justify-between items-center">
    <h1 class="text-2xl font-bold">E-Library</h1>
    <ul class="flex space-x-4">
      <li>
        <router-link to="/profile" class="hover:text-gray-300" v-if="showProfileLink">
          Profile
        </router-link>
      </li>
      <li>
        <router-link to="/books" class="hover:text-gray-300">Library</router-link>
      </li>
      <!-- Add other navigation links here -->
    </ul>
  </nav>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue'
import { useRoute } from 'vue-router'

export default defineComponent({
  name: 'Navbar',
  setup() {
    const route = useRoute()

    const showNavbar = computed(() => {
      return !['/register', '/login', '/'].includes(route.path)
    })

    const showProfileLink = computed(() => {
      return !['/register', '/login'].includes(route.path)
    })

    return {
      showNavbar,
      showProfileLink
    }
  }
})
</script>

<style scoped>
/* Add any additional styling if needed */
</style>
