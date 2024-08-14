<script lang="ts">
import { defineComponent } from 'vue'
import Navbar from './components/NavBar.vue'

export default defineComponent({
  name: 'App',
  components: {
    Navbar
  }
})
</script>

<template>
  <div id="app" class="container mx-auto px-4">
    <Navbar />
    <router-view />
  </div>
</template>

<style>
/* #app { */
/* max-width: 1260px; */
/* max-height: 100vh; */
/* margin: 0 auto; */
/* padding: 2rem; */
/* font-weight: normal; */
/* } */
</style>
