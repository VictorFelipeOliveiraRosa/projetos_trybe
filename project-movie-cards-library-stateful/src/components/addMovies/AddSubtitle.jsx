import React, { Component } from 'react';
import PropTypes from 'prop-types';

class AddSubtitle extends Component {
  render() {
    const { subtitle, handleChange } = this.props;
    return (
      <div>
        <label data-testid="subtitle-input-label" htmlFor="subtitle">
          Subtítulo
          <input
            data-testid="subtitle-input"
            type="text"
            name="subtitle"
            onChange={ handleChange }
            value={ subtitle }
          />
        </label>
      </div>
    );
  }
}

AddSubtitle.propTypes = {
  subtitle: PropTypes.string,
  handleChange: PropTypes.func,
};

AddSubtitle.defaultProps = {
  subtitle: '',
  handleChange: () => {},
};

export default AddSubtitle;
