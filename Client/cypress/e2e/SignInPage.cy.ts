describe('SignInPage', () => {

  beforeEach(() => {

    cy.visit('http://localhost:3000/signin');

  });

  it('should render the SignInPage successfully with the expected content.', () => {

    cy.contains('CONNEXION').should('exist');

  });

});