import { ref, computed, nextTick } from 'vue'
import { defineStore } from 'pinia'

// export const useCounterStore = defineStore('counter', () => {
//   const count = ref(0)
//   const doubleCount = computed(() => count.value * 2)
//   async function increment() {
//     count.value++
//     // await nextTick()
//   }

//   return { count, doubleCount, increment }
// })

export default {
  setup() {
    const count = ref(0)

    const doubleCount = computed(() => count.value * 2)

    async function increment() {
      count.value++
      await nextTick()
    }

    return { count, increment, doubleCount }
  }
}
