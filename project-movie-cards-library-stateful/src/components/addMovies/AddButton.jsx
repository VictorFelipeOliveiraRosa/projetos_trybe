import React, { Component } from 'react';
import PropTypes from 'prop-types';

class AddButton extends Component {
  render() {
    const { onClick } = this.props;
    return (
      <div>
        <button data-testid="send-button" type="button" onClick={ onClick }>
          Adicionar filme
        </button>
      </div>
    );
  }
}

AddButton.propTypes = {
  onClick: PropTypes.func,
};

AddButton.defaultProps = {
  onClick: () => {},
};

export default AddButton;
