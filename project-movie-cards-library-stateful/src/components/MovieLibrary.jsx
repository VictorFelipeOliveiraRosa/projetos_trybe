import React, { Component } from 'react';
import PropTypes from 'prop-types';

import MovieList from './MovieList';
import SearchBar from './SearchBar';
import AddMovie from './AddMovie';

class MovieLibrary extends Component {
  constructor(props) {
    super(props);

    const { movies } = this.props;

    this.state = {
      bookmarkedOnly: false,
      searchText: '',
      selectedGenre: '',
      movies,
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleFilter = this.handleFilter.bind(this);
    this.handFilterBook = this.handFilterBook.bind(this);
    this.handleAddMovie = this.handleAddMovie.bind(this);
  }

  handleChange(event) {
    const { target } = event;
    if (target.type !== 'checkbox') {
      this.setState({ [target.name]: target.value });
    } else {
      this.setState({ [target.name]: target.checked });
    }
  }

  handleFilter(movies) {
    const { searchText, bookmarkedOnly, selectedGenre } = this.state;
    const moviesResults = movies.filter((movie) => {
      if (selectedGenre === movie.genre) return movie;
      if (selectedGenre === '') return movie;
      return '';
    }).filter((movie) => {
      if (searchText === '' || searchText === ' ') return movie;
      if (movie.title.toLowerCase().includes(searchText.toLowerCase())
        || movie.subtitle.toLowerCase().includes(searchText.toLowerCase())
        || movie.storyline.toLowerCase().includes(searchText.toLowerCase())
      ) {
        return movies;
      }
      return undefined;
    });
    return this.handFilterBook(bookmarkedOnly, moviesResults);
  }

  handleAddMovie(newMovie) {
    this.setState((currentState) => ({
      movies: [...currentState.movies, newMovie],
    }));
  }

  handFilterBook(bookmarkedOnly, movies) {
    return movies.filter((movie) => {
      if (!bookmarkedOnly) return movie;
      if (bookmarkedOnly === movie.bookmarked && bookmarkedOnly) {
        return movie;
      }
      return '';
    });
  }

  render() {
    const { bookmarkedOnly, searchText, selectedGenre, movies } = this.state;
    const moviesN = this.handleFilter(movies);
    return (
      <div>
        <h2> My awesome movie library </h2>
        <SearchBar
          bookmarkedOnly={ bookmarkedOnly }
          searchText={ searchText }
          selectedGenre={ selectedGenre }
          onSearchTextChange={ this.handleChange }
          onBookmarkedChange={ this.handleChange }
          onSelectedGenreChange={ this.handleChange }
        />
        <MovieList movies={ moviesN } />
        <AddMovie onClick={ this.handleAddMovie } />
      </div>
    );
  }
}

MovieLibrary.propTypes = {
  movies: PropTypes.arrayOf(PropTypes.shape()),
};

MovieLibrary.defaultProps = {
  movies: [],
};

export default MovieLibrary;
