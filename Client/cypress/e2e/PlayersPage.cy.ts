describe('PlayersPage', () => {

  beforeEach(() => {

    cy.visit('http://localhost:3000/players');

  });

  it('should render the PlayersPage successfully with the expected content.', () => {

    cy.contains('Barre de recherche').should('exist');

  });

});