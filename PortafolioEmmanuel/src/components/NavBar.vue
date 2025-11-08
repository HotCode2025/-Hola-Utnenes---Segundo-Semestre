<script setup>
const github = "https://github.com/Emmanuel3843";
const instagram = "https://instagram.com/emmanuel.poletto";
</script>

<template>
  <nav class="navbar">
    <ul>
      <li><a :href="github" target="_blank">GitHub</a></li>
      <li><a :href="instagram" target="_blank">Instagram</a></li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  background: #1a73e8;
  padding: 1rem;
}

ul {
  display: flex;
  gap: 1.5rem;
  list-style: none;
  justify-content: center;
}

a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

a:hover {
  text-decoration: underline;
}
</style>
