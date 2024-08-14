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
  <div id="app">
    <Navbar />
    <router-view />
  </div>
</template>

<style>
/* Global styles */
</style>
