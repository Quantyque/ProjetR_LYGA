describe('RegisterPage', () => {

  beforeEach(() => {

    cy.visit('http://localhost:3000/register');

  });

  it('should render the RegisterPage successfully with the expected content.', () => {

    cy.contains('INSCRIPTION').should('exist');

  });

});