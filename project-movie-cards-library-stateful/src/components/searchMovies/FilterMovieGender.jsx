import React, { Component } from 'react';
import PropTypes from 'prop-types';

class FilterMovieGender extends Component {
  createGenderOptions(selectedGenre, onSelectedGenreChange) {
    return (
      <select
        value={ selectedGenre }
        data-testid="select-input"
        name="selectedGenre"
        onChange={ onSelectedGenreChange }
      >
        <option data-testid="select-option" defaultChecked value="">Todos</option>
        <option data-testid="select-option" value="action">Ação</option>
        <option data-testid="select-option" value="comedy">Comédia</option>
        <option data-testid="select-option" value="thriller">Suspense</option>
      </select>);
  }

  render() {
    const { selectedGenre, onSelectedGenreChange } = this.props;
    return (
      <div>
        <label data-testid="select-input-label" htmlFor="selectedGenre">
          Filtrar por gênero
          { this.createGenderOptions(selectedGenre, onSelectedGenreChange) }
        </label>
      </div>
    );
  }
}

FilterMovieGender.propTypes = {
  selectedGenre: PropTypes.string.isRequired,
  onSelectedGenreChange: PropTypes.func.isRequired,
};

// FilterMovieGender.defaultProps = {
//   selectedGenre: '',
//   onSelectedGenreChange: () => {},
// };

export default FilterMovieGender;
