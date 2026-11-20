import React from 'react';
import { createFrontendModule } from '@backstage/frontend-plugin-api';
import { EntityContentBlueprint } from '@backstage/plugin-catalog-react/alpha';
import { compatWrapper } from '@backstage/core-compat-api';
import { EntityJenkinsContent } from '@backstage-community/plugin-jenkins';

const jenkinsEntityContent = EntityContentBlueprint.make({
  name: 'jenkins',
  params: {
    defaultPath: '/jenkins',
    defaultTitle: 'Jenkins',
    loader: () =>
      Promise.resolve(compatWrapper(<EntityJenkinsContent />)),
  },
});

export const jenkinsModule = createFrontendModule({
  pluginId: 'catalog',
  extensions: [jenkinsEntityContent],
});