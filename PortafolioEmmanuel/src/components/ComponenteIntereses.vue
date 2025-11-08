<script setup>
const intereses = [
  "Videojuegos",
  "Creación de páginas web",
  "Programar"
];
</script>

<template>
  <section class="intereses">
    <h2>Intereses</h2>
    <ul>
      <li v-for="i in intereses" :key="i">{{ i }}</li>
    </ul>
  </section>
</template>

<style scoped>
.intereses {
  padding: 2rem;
  background: #d9ecff;
  border-radius: 12px;
  margin: 1.5rem;
}

h2 {
  color: #1a73e8;
  text-align: center;
  margin-bottom: 1rem;
}

ul {
  list-style: none;
  padding: 0;
  text-align: center;
}

li {
  padding: 0.5rem 0;
  font-size: 1.1rem;
  color: #0a2a43;
}
</style>