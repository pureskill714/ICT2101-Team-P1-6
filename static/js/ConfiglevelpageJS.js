const board = document.getElementById("board");
const newGameButton = document.getElementById("newGame");
const saveGameButton = document.getElementById("saveGame");
const grid3Button = document.getElementById("3by3");
const grid4Button = document.getElementById("4by4");
const grid5Button = document.getElementById("5by5");
const grid6Button = document.getElementById("6by6");
const easyDiffButton = document.getElementById("easy");
const mediumDiffButton = document.getElementById("medium");
const hardDiffButton = document.getElementById("hard");

const currentRowNum = 3;
let currentColumnNum = 3;
let firstItem = true;
let gameState = Array(currentRowNum*currentColumnNum).fill(0);
let currentDifficulty = easyDiffButton;


const drawBoard = (gridSize) =>{
    board.innerHTML = "";
    board.style.gridTemplateColumns = `repeat(${gridSize}, 70px)`;
    board.style.gridTemplateRows = `repeat(${currentRowNum}, 70px)`;
    board.style.gridGap = "2px";
    for (let index = 0; index < gameState.length; index++) {
        const newDiv = document.createElement("div");
        newDiv.setAttribute("id", `space${index}`);
        newDiv.setAttribute("onclick",`toggleColour(${newDiv.id})`);
        newDiv.style.backgroundColor = "#000";
        newDiv.style.border = "2px solid red";
        board.appendChild(newDiv);
        
    }
};

const toggleColour = (element) =>{
    if (firstItem){
        element.innerHTML = "Start";
        element.style.font = "20px Arial, sans-serif";
        element.style.color = "red";
        firstItem = false;
    }
    
    const index = `${element.id}`.slice(-1);
    const boxState = gameState[index];
    if (boxState == 0){
        element.style.backgroundColor = "#FFF";
        gameState[index] = 1;
    }else{
        element.style.backgroundColor = "#000";
        gameState[index] = 0;
    }
    
};

const changeGridSize = (size) =>{
    currentColumnNum = size;
    gameState = Array(currentRowNum*currentColumnNum).fill(0);
    drawBoard(currentColumnNum);
    firstItem = true;
};

const changeDifficulty = (difficulty) =>{
    currentDifficulty.disabled = !currentDifficulty.disabled;
    difficulty.disabled = !difficulty.disabled;
    currentDifficulty = difficulty;

};

const startNewGame = () =>{
    gameState = Array(currentRowNum*currentColumnNum).fill(0);
    drawBoard(currentColumnNum);
    firstItem = true;
};

const saveGame =() =>{
    const blob = new Blob([JSON.stringify(gameState)],{type:'application/json'});
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "gameState.txt";
    a.click();
};

drawBoard(currentColumnNum);
easyDiffButton.setAttribute("onclick",`changeDifficulty(${easyDiffButton.id})`);
mediumDiffButton.setAttribute("onclick",`changeDifficulty(${mediumDiffButton.id})`);
hardDiffButton.setAttribute("onclick",`changeDifficulty(${hardDiffButton.id})`);
currentDifficulty.disabled = true;
