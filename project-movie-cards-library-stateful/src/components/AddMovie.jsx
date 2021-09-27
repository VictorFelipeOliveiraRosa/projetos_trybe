// implement AddMovie component here
import React, { Component } from 'react';
import PropTypes from 'prop-types';

import AddTitle from './addMovies/AddTitle';
import AddSubtitle from './addMovies/AddSubtitle';
import AddImagePath from './addMovies/AddImagePath';
import AddRating from './addMovies/AddRating';
import AddGenre from './addMovies/AddGenre';
import AddStoryLine from './addMovies/AddStoryLine';
import AddButton from './addMovies/AddButton';

class AddMovie extends Component {
  constructor() {
    super();
    this.state = {
      subtitle: '',
      title: '',
      imagePath: '',
      storyline: '',
      rating: 0,
      genre: 'action',
    };
    this.handleChange = this.handleChange.bind(this);
    this.resetState = this.resetState.bind(this);
    this.onAddMovie = this.onAddMovie.bind(this);
  }

  handleChange(event) {
    const { target } = event;
    this.setState({ [target.name]: target.value });
  }

  onAddMovie(event) {
    event.preventDefault();
    const { onClick } = this.props;
    const { subtitle, title, imagePath, storyline, rating, genre } = this.state;
    const movie = {
      subtitle,
      title,
      imagePath,
      storyline,
      rating,
      genre,
    };
    onClick(movie);
    this.resetState();
  }

  resetState() {
    this.setState({
      subtitle: '',
      title: '',
      imagePath: '',
      storyline: '',
      rating: 0,
      genre: 'action',
    });
  }

  render() {
    const { subtitle, title, imagePath, storyline, rating, genre } = this.state;
    return (
      <div>
        <form data-testid="add-movie-form" action="#">
          <AddTitle handleChange={ this.handleChange } title={ title } />
          <AddSubtitle handleChange={ this.handleChange } subtitle={ subtitle } />
          <AddImagePath handleChange={ this.handleChange } imagePath={ imagePath } />
          <AddStoryLine handleChange={ this.handleChange } storyline={ storyline } />
          <AddRating handleChange={ this.handleChange } rating={ Number(rating) } />
          <AddGenre handleChange={ this.handleChange } genre={ genre } />
          <AddButton onClick={ this.onAddMovie } />
        </form>
      </div>
    );
  }
}

AddMovie.propTypes = {
  onClick: PropTypes.func,
};

AddMovie.defaultProps = {
  onClick: () => {},
};

export default AddMovie;
