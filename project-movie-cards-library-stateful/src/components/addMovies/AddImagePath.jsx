import React, { Component } from 'react';
import PropTypes from 'prop-types';

class AddImagePath extends Component {
  render() {
    const { imagePath, handleChange } = this.props;
    return (
      <div>
        <label data-testid="image-input-label" htmlFor="imagePath">
          Imagem
          <input
            data-testid="image-input"
            type="text"
            name="imagePath"
            onChange={ handleChange }
            value={ imagePath }
          />
        </label>
      </div>
    );
  }
}

AddImagePath.propTypes = {
  imagePath: PropTypes.string,
  handleChange: PropTypes.func,
};

AddImagePath.defaultProps = {
  imagePath: '',
  handleChange: () => {},
};

export default AddImagePath;
