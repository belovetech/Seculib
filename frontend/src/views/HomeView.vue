<script setup>
// import { ref } from 'vue'
import counterStore from './../stores/counter'

const { count, increment, doubleCount } = counterStore.setup()
</script>

<template>
  <div class="home">
    <p>Count: {{ count }}</p>
    <p>Double Count: {{ doubleCount }}</p>
    <button @click="increment">increment</button>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
