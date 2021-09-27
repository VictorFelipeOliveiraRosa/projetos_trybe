import React, { Component } from 'react';
import PropTypes from 'prop-types';

class AddGenre extends Component {
  createGenderOptions(genre, handleChange) {
    return (
      <select
        value={ genre }
        data-testid="genre-input"
        name="genre"
        onChange={ handleChange }
      >
        <option data-testid="genre-option" value="action" checked>Ação</option>
        <option data-testid="genre-option" value="comedy">Comédia</option>
        <option data-testid="genre-option" value="thriller">Suspense</option>
      </select>);
  }

  render() {
    const { genre, handleChange } = this.props;
    return (
      <div>
        <label data-testid="genre-input-label" htmlFor="genre">
          Gênero
          { this.createGenderOptions(genre, handleChange) }
        </label>
      </div>
    );
  }
}

AddGenre.propTypes = {
  genre: PropTypes.string,
  handleChange: PropTypes.func,
};

AddGenre.defaultProps = {
  genre: 'action',
  handleChange: () => {},
};

export default AddGenre;
