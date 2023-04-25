<script>
  export let poster = "";
  export let name = "";
  export let imdb_id = "";
</script>

<div class="w-fit m-6 border rounded-md shadow bg-gray-700 border-gray-800">
  <div class="">
    <a href={"/movie/" + imdb_id}>
      <img
        class="rounded-t-md h-72 w-48"
        src={"http://image.tmdb.org/t/p/w200" + poster}
        alt="" />
    </a>
  </div>
  <div class="flex flex-col p-2 text-center">
    <a href={"/movie/" + imdb_id}>
      <h5
        class="w-44 mb-2 text-lg font-bold font-poppins text-slate-300 hover:text-white">
        {name}
      </h5>
    </a>
  </div>
</div>
