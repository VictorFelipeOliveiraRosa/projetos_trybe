import React, { Component } from 'react';
import PropTypes from 'prop-types';

class CheckMovieFavorite extends Component {
  render() {
    const { bookmarkedOnly, onBookmarkedChange } = this.props;
    return (
      <div>
        <label data-testid="checkbox-input-label" htmlFor="bookmarkedOnly">
          Mostrar somente favoritos
          <input
            data-testid="checkbox-input"
            name="bookmarkedOnly"
            type="checkbox"
            defaultChecked={ bookmarkedOnly }
            value="favorite"
            onChange={ onBookmarkedChange }
          />
        </label>
      </div>
    );
  }
}

CheckMovieFavorite.propTypes = {
  bookmarkedOnly: PropTypes.bool,
  onBookmarkedChange: PropTypes.func,
};

CheckMovieFavorite.defaultProps = {
  bookmarkedOnly: false,
  onBookmarkedChange: () => {},
};

export default CheckMovieFavorite;
