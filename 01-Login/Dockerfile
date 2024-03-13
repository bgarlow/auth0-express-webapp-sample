FROM node:20.11.1-bullseye-slim
ENV NODE_ENV production
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]