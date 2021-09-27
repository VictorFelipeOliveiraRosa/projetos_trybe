/* eslint-disable react/prop-types */
import React, { Component } from 'react';
import PropTypes, { number, string } from 'prop-types';
import MovieCard from './MovieCard';

class MovieList extends Component {
  render() {
    const { movies } = this.props;
    return (
      <div key="card-content" className="movie-list">
        { movies.map((movie) => (
          <MovieCard key={ movie.title } movie={ movie } />
        )) }
      </div>
    );
  }
}

MovieList.propTypes = {
  movies: PropTypes.arrayOf(
    PropTypes.shape({
      title: string.isRequired,
      subtitle: string.isRequired,
      storyline: string.isRequired,
      rating: number.isRequired,
      imagePath: string.isRequired,
    }),
  ).isRequired,
};

export default MovieList;
