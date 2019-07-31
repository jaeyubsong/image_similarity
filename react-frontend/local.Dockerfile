FROM node:10.15.3

RUN npm install react-scripts@2.1.8 -g --silent

WORKDIR /usr/src/app

ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY package.json /usr/src/app/package.json
RUN npm install --silent

CMD ["npm", "start"]