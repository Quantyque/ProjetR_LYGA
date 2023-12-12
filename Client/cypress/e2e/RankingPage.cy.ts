describe('RankingPage', () => {

  beforeEach(() => {

    cy.visit('http://localhost:3000/ranking');

  });

  it('should render the RankingPage successfully with the expected content.', () => {

    cy.contains('Place').should('exist');
    cy.contains('Profil').should('exist');
    cy.contains('Équipe(s) | Nom').should('exist');
    cy.contains('Score').should('exist');
    cy.contains('Jeu').should('exist');
    cy.contains('Saison').should('exist');

  });

});