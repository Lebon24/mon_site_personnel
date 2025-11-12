FROM node:18-bookworm

RUN apt-get update && apt-get install -y libpq5

WORKDIR /app

COPY package*.json ./
RUN npm install


COPY . .

CMD ["npm", "start"]
