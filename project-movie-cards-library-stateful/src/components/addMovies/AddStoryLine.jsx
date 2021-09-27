import React, { Component } from 'react';
import PropTypes from 'prop-types';

class AddStoryLine extends Component {
  render() {
    const { storyline, handleChange } = this.props;
    return (
      <div>
        <label data-testid="storyline-input-label" htmlFor="storyline">
          Sinopse
          <textarea
            data-testid="storyline-input"
            type="textarea"
            name="storyline"
            onChange={ handleChange }
            value={ storyline }
          />
        </label>
      </div>
    );
  }
}

AddStoryLine.propTypes = {
  storyline: PropTypes.string,
  handleChange: PropTypes.func,
};

AddStoryLine.defaultProps = {
  storyline: '',
  handleChange: () => {},
};

export default AddStoryLine;
