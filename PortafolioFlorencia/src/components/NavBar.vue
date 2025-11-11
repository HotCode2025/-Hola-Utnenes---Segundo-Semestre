<template>
  <nav class="navbar">
    <ul>
      <li><a href="#educacion">Educación</a></li>
      <li><a href="#experiencia">Experiencia</a></li>
      <li><a href="#proyectos">Proyectos</a></li>
      <li><a href="#habilidades">Habilidades</a></li>
      <li><a href="#intereses">Intereses</a></li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: #4b0082;
  text-align: center;
  padding: 15px 10px;
}

.navbar ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: center;
  flex-wrap: wrap; 
  gap: 30px;
}

.navbar ul li a {
  color: white;
  text-decoration: none;
  font-size: 2rem;
  font-weight: bold;
  transition: color 0.3s ease;
}

.navbar ul li a:hover {
  color: #ffccff;
}


@media (max-width: 768px) {
  .navbar ul {
    gap: 15px;
  }

  .navbar ul li a {
    font-size: 1.5rem;
  }
}

@media (max-width: 480px) {
  .navbar ul {
    gap: 10px;
  }

  .navbar ul li a {
    font-size: 1.2rem;
  }
}
</style>
