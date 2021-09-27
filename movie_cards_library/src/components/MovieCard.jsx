import React, { Component } from 'react';
import PropTypes, { number, string } from 'prop-types';
import Rating from './Rating';


class MovieCard extends Component {
  render() {
    const { movie: { title, subtitle, storyline, rating, imagePath } } = this.props;
    return (
      <div className="card-container">
        <div className="movie-card-back">
          <div className="card-image">
            <img src={ imagePath } alt="poster" />
          </div>
          <div className="card-title"><h4>{ title }</h4></div>
          <div className="card-subtitle">
            <h5>{ subtitle }</h5>
          </div>
          <div className="cae"><p>{ storyline }</p></div>
          <div className="card-rating">
            <Rating rating={ rating } />
          </div>
        </div>
      </div>
    );
  }
}

MovieCard.propTypes = {
  movie: PropTypes.shape({
    title: string.isRequired,
    subtitle: string.isRequired,
    storyline: string.isRequired,
    rating: number.isRequired,
    imagePath: string.isRequired,
  }).isRequired,
};

export default MovieCard;
