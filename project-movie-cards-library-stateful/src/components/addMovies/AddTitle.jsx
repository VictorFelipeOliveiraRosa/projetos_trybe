import React, { Component } from 'react';
import PropTypes from 'prop-types';

class AddTitle extends Component {
  render() {
    const { title, handleChange } = this.props;
    return (
      <div>
        <label data-testid="title-input-label" htmlFor="title">
          Título
          <input
            data-testid="title-input"
            type="text"
            name="title"
            onChange={ handleChange }
            value={ title }
          />
        </label>
      </div>
    );
  }
}

AddTitle.propTypes = {
  title: PropTypes.string,
  handleChange: PropTypes.func,
};

AddTitle.defaultProps = {
  title: '',
  handleChange: () => {},
};

export default AddTitle;
