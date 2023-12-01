describe('HomePage', () => {

  beforeEach(() => {

    cy.visit('http://localhost:3000/home');

  });

  it('should render the HomePage successfully with the expected content.', () => {

    cy.contains('Ranking').should('exist');
    cy.contains('Community').should('exist');
    cy.contains('Guides').should('exist');
    cy.contains('Players').should('exist');
    cy.contains('Tournaments').should('exist');

  });

});