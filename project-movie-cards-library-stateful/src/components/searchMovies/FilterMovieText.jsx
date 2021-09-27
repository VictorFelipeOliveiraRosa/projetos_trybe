import React, { Component } from 'react';
import PropTypes from 'prop-types';

class FilterMovieText extends Component {
  render() {
    const { searchText, onSearchTextChange } = this.props;
    return (
      <div>
        <label data-testid="text-input-label" htmlFor="searchText">
          Inclui o texto:
          <input
            data-testid="text-input"
            name="searchText"
            type="text"
            value={ searchText }
            onChange={ onSearchTextChange }
          />
        </label>
      </div>
    );
  }
}

FilterMovieText.propTypes = {
  searchText: PropTypes.string,
  onSearchTextChange: PropTypes.func,
};

FilterMovieText.defaultProps = {
  searchText: '',
  onSearchTextChange: () => {},
};

export default FilterMovieText;
