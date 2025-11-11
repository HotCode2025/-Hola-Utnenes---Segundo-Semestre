<template>
  <section id="intereses" class="intereses">
    <h2>Intereses</h2>
    <div class="cards">
      <div class="card">
        <h3>🌍 Compromiso con el medio ambiente</h3>
        <p>
          Promover el uso responsable de la tecnología para reducir el impacto ambiental, impulsando soluciones digitales sostenibles y prácticas de consumo consciente.
        </p>
      </div>

      <div class="card">
        <h3>🔒 Ciberseguridad y privacidad</h3>
        <p>
          Me interesa el desarrollo de sistemas seguros que protejan la información y fomenten la confianza en el uso de la tecnología.
        </p>
      </div>

      <div class="card">
        <h3>💡 Innovación y educación tecnológica</h3>
        <p>
          Creo en la educación como motor del cambio, y busco integrar la tecnología en espacios educativos para potenciar el aprendizaje y la inclusión digital.
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.intereses {
  background: linear-gradient(135deg, #e0baff, #c18bff, #a355ff);
  padding: 60px 30px;
  border-radius: 25px;
  width: 90%;
  margin: 40px auto;
  text-align: center;
  color: black;
}

h2 {
  font-size: 2.5rem;
  margin-bottom: 30px;
  font-weight: bold;
}

.cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 25px;
}

.card {
  background-color: #d8b4ff;
  color: black;
  border-radius: 40px;
  padding: 25px;
  width: 300px;
  max-width: 100%;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: left;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
}

.card h3 {
  font-size: 1.8rem;
  margin-bottom: 10px;
}

.card p {
  font-size: 1.5rem;
  line-height: 1.5;
}


@media (max-width: 1024px) {
  .card {
    padding: 20px;
  }
  .card h3 {
    font-size: 1.6rem;
  }
  .card p {
    font-size: 1.4rem;
  }
}

@media (max-width: 768px) {
  .cards {
    flex-direction: column;
    align-items: center;
  }
  .card {
    width: 90%;
    padding: 18px;
  }
  .card h3 {
    font-size: 1.5rem;
  }
  .card p {
    font-size: 1.3rem;
  }
}

@media (max-width: 480px) {
  .intereses {
    padding: 40px 15px;
  }
  h2 {
    font-size: 2rem;
    margin-bottom: 20px;
  }
  .card h3 {
    font-size: 1.3rem;
  }
  .card p {
    font-size: 1.2rem;
  }
}
</style>
