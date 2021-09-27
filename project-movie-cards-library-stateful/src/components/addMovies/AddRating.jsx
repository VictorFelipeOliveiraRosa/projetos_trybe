import React, { Component } from 'react';
import PropTypes from 'prop-types';

class AddRating extends Component {
  render() {
    const { rating, handleChange } = this.props;
    return (
      <div>
        <label data-testid="rating-input-label" htmlFor="rating">
          Avaliação
          <input
            data-testid="rating-input"
            type="number"
            name="rating"
            onChange={ handleChange }
            value={ rating }
          />
        </label>
      </div>
    );
  }
}

AddRating.propTypes = {
  rating: PropTypes.number,
  handleChange: PropTypes.func,
};

AddRating.defaultProps = {
  rating: 0,
  handleChange: () => {},
};

export default AddRating;
