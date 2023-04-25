// @ts-nocheck
export const load = async ({ params, fetch }) => {
  const loadmovie = async () => {
    let res = await fetch(
      `https://api.themoviedb.org/3/movie/${params.slug}?api_key=843811a4e70cd56397b52a070f1ddf61`
    );
    let info = await res.json();
    let movieinfo = {
      backdrop: "https://image.tmdb.org/t/p/original",
      poster: "https://image.tmdb.org/t/p/w300",
      title: "",
      year: "",
      tagline: "",
      overview: "",
    };
    if (info) {
      movieinfo.poster += info["poster_path"];
      movieinfo.backdrop += info["backdrop_path"];
      movieinfo.title = info["original_title"];
      movieinfo.overview = info["overview"];
      movieinfo.tagline = info["tagline"];
      movieinfo.year = info["release_date"].slice(0, 4);
    }
    return movieinfo;
  };

  let director = { name: "", profile_path: "" };
  const loadcast = async () => {
    let res = await fetch(
      `https://api.themoviedb.org/3/movie/${params.slug}/credits?api_key=843811a4e70cd56397b52a070f1ddf61`
    );
    let info = await res.json();
    for (let i = 0; i < info["crew"].length; i++) {
      if (info["crew"][i]["job"] === "Director") {
        director = info["crew"][i];
      }
    }
    return info["cast"].slice(0, 5);
  };

  const [movieinfo, cast] = await Promise.all([loadmovie(), loadcast()]);
  //   let movieinfo = await loadmovie();
  //   let cast = await loadcast();

  return {
    slug: params.slug,
    movieinfo: movieinfo,
    director: director,
    cast: cast,
  };
};
