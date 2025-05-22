console.log("Página carregada com sucesso.");
// Exemplo: mostrar alerta ao clicar em um card
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('click', () => {
    alert(`Você clicou em: ${card.textContent}`);
  });
});
