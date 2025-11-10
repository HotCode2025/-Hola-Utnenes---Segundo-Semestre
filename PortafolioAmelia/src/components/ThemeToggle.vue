<template>
  <button @click="toggleTheme" class="theme-toggle">🌓</button>
</template>

<script setup>
const toggleTheme = () => {
  const body = document.body
  if(body.classList.contains('light-mode')){ body.classList.remove('light-mode'); body.classList.add('dark-mode') }
  else { body.classList.remove('dark-mode'); body.classList.add('light-mode') }
}
document.body.classList.add('light-mode')
</script>

<style scoped>
/* Estilos ThemeToggle */
</style>