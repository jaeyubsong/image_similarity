import React, { useState, useEffect } from 'react';
//import logo from '../../assets/images/logo.svg';
import './App.css';
import axios from 'axios'
import Grid from '@material-ui/core/Grid'



//const BASE_URI = 'http://localhost:5000'



function App() {
  const [count, setCount] = useState(0);
  const [data, setData] = useState({ hits: [] });
  const [similarity, setSimilarity] = useState(0);

  const [originalImageListResult, setOriginalImageListResult] = useState([])
  const [imageListResult, setImageListResult] = useState([])


  const fetchData = async () => {
    console.log("fetchData is called");
    const result = await axios({
      method: 'post',
      url: 'http://localhost:5000/vbs/getData',
      headers: {
        "Access-Control-Allow-Origin": "*"
      }
    });
    // console.log(result.data)
    // const myData = result.data.map(value => (
    //   require('../..' + value.path)
    // ))
    // const tempImageListResult = {...result.data}
    console.log("# of frames before processing: " + result.data.length)
    setOriginalImageListResult(result.data)
    const newImageListResult = []
    
    let tempImageListResult = []
    for (let i = 0; i < result.data.length; i++) {
      tempImageListResult.push(result.data[i])
      if (result.data[i].isLast == true || result.data[i].similarity > similarity) {
        // const tmp = {...tempImageListResult}
        // console.log(tmp)
        newImageListResult.push(tempImageListResult)
        tempImageListResult = []
      }
    }
    console.log("# of frames after processing: " + newImageListResult.length)
    // console.log("new image result is: ")
    // console.log(newImageListResult)
    // Object.assign(newImageListResult, {data: result.data})

    // Process data
    setImageListResult(newImageListResult)

  }

  const changeSimilarityThreshold = similarity => {
    console.log("# of frames before processing: " + originalImageListResult.length)
    const newImageListResult = []
    
    let tempImageListResult = []
    for (let i = 0; i < originalImageListResult.length; i++) {
      tempImageListResult.push(originalImageListResult[i])
      if (originalImageListResult[i].isLast == true || originalImageListResult[i].similarity > similarity) {
        // const tmp = {...tempImageListResult}
        // console.log(tmp)
        newImageListResult.push(tempImageListResult)
        tempImageListResult = []
      }
    }
    console.log("# of frames after processing: " + newImageListResult.length)
    // console.log("new image result is: ")
    // console.log(newImageListResult)
    // Object.assign(newImageListResult, {data: result.data})

    // Process data
    setImageListResult(newImageListResult)
  }



  return (
    <div className="App">
      <div>
        <p>You clicked me {count} times</p>
        <button onClick={() => {
          console.log("Increase count");
          setCount(count + 1);
          setData({ hits: [count] });
        }}>
          click to increase count
        </button>
        <button onClick={() => {
          console.log("Call fetchData");
          fetchData();
        }}>
          Reload database
        </button>
        <input style={{width: "100px"}} type="number" value={similarity} onChange={(event) => {
                      setSimilarity(parseInt(event.target.value))
        }} />
        <button onClick={() => {
          console.log("Change similarity");
          changeSimilarityThreshold(similarity);
        }}>
          similarity
        </button>

      </div>
      {imageListResult.map((value, index) => (
        <Grid key={index} container key={index}>
          {value.map((mValue, mIndex) => 
              <Grid key={mValue.path} item padding={5}>
                <img key={mValue.path} src={process.env.PUBLIC_URL + mValue.path} style={{ width: 300}} />
                {mValue.similarity.toFixed(3)}
              </Grid>
            )}
          <Grid item xs={12}>
            <br /><br />New section<br /><br /><br />
          </Grid>
        </Grid>
      ))}
    </div>

  );
};

export default App;
